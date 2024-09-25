import React, { useRef, useState } from 'react'
import TagsList from '../components/common/TagsList.jsx'
import '../styles/components/TagsList.css'

const TagsBox = (props) => {
  // const inputRef = useRef(null);
  const [inputValue, setInputValue] = useState('');

  const addTag = (e) => {
    if (e.key !== 'Enter') return;
    e.preventDefault();
    createTags();
    setInputValue('');
  };

  const createTags = () => {
    // const inputElem = inputRef.current;
    // if (inputElem == null) { console.log('tagsBox not found'); return; }
    // const tagsString = inputElem.value?.replace(/\s+/g, ' ') ?? "";
    // const tagsList = tagsString.split(',');

    const tagsString = inputValue?.replace(/\s+/g, ' ') ?? "";
    const tagsList = tagsString.split(',');
    
    props.setTags((prevTags) => Array.from(new Set([...prevTags, ...tagsList])))
    // inputElem.value = '';
  }
  const handleInputChange = (e) => {
    setInputValue(e.target.value)
  }
  
  return (
    <div className="tags-box">
      <label htmlFor="metric-area" className="form-label">{props.label}</label>
      <span className="input-note d-block">Please add a comma after each tag and press enter</span>
      <div className="box">
        <TagsList tags={props.tags} setTags={props.setTags}/>
        <input
          value={inputValue}
          type="text"
          onKeyDown={addTag}
          onChange={(e) => handleInputChange(e)}
        />
      </div>
    </div>
  );
}

export default TagsBox;