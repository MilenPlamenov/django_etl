import React, { useState, useEffect } from 'react';

const Articles = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const defaultImage = '../public/default.png'

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/articles/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setArticles(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

console.log(articles);
  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Articles</h1>
      <div className="row">
        {articles.map(article => (
          <div className="col-md-4 mb-4" key={article.id}>
            <div className="card h-100">
              <div className="image-container">
                <img src={article.image_urls || defaultImage} alt={article.title} className="card-img-top" />
              </div>
              <div className="card-body">
                <h5 className="card-title">{article.title}</h5>
                <h6 className="card-subtitle mb-2 text-muted">By {article.author}</h6>
                <p className="card-text">
                  <small className="text-muted">{new Date(article.publication_date).toLocaleDateString()}</small>
                </p>
                <p className="card-text">{article.body}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Articles;