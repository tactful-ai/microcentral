import React from 'react'

const TagsList = ({ tags, setTags }) => {

  const removeTag = (tagName) => {
    setTags((tags) => tags.filter(tag => tag != tagName));
  };

  return (
    <ul id="metric-area">
      {tags?.map((tag, index) => (
        <li key={index}>
          {tag} <button type="button" className="tag-cancel" onClick={() => removeTag(tag)}>
            <i className="fas fa-times"></i></button>
        </li>
      ))}
    </ul>
  );

}
export default TagsList