import React from 'react'

const TagsList = ({ tags, setTags, serviceIds }) => {

  const removeTag = (tagId) => {
    // setTags((tags) => tags.filter(tag => tag.id != tagId));
    setTags((prevTags) => {
      const updatedTags = tags.filter(tag => tag.id != tagId);
      serviceIds(updatedTags);
      console.log('Updated service tags: ', updatedTags);
      return updatedTags; 
    });
    console.log('tag removed: id: ', tagId)
    console.log('tags: ', tags)
  };

  return (
    <ul id="metric-area">
      {tags?.map((tag) => (
        <li key={tag.id}>
          {tag.name} 
          <button type="button" className="tag-cancel" onClick={() => removeTag(tag.id)}>
            <i className="fas fa-times"></i></button>
        </li>
      ))}
    </ul>
  );

}
export default TagsList