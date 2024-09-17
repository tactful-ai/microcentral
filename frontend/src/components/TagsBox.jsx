import React, { useRef } from 'react'
import TagsList from '../components/common/TagsList.jsx'
import '../styles/components/TagsBox.css'

const TagsBox = (props) => {
  const inputRef = useRef(null);

  const addTag = (e) => {
    if (e.key !== 'Enter') return;
    e.preventDefault();
    createTags();
  };

  const createTags = () => {
    const inputElem = inputRef.current;
    if (inputElem == null) { console.log('tagsBox not found'); return; }
    const tagsString = inputElem.value?.replace(/\s+/g, ' ') ?? "";
    const tagsList = tagsString.split(',');
    
    props.setTags((prevTags) => Array.from(new Set([...prevTags, ...tagsList])))
    inputElem.value = '';
  }
  
  return (
    <div className="tags-box">
      <label htmlFor="metric-area" className="form-label">{props.label}</label>
      <span className="input-note d-block">Please add a comma after each tag and press enter</span>
      <div className="box">
        <TagsList tags={props.tags} setTags={props.setTags}/>
        <input
          ref={inputRef}
          type="text"
          onKeyDown={addTag}
        />
      </div>
    </div>
  );
}

export default TagsBox;