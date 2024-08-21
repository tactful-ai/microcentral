
let form = document.querySelector('form');
let scorecardName = form.querySelector('#scorecard-name');
let metricsSelect = form.querySelector('#scorecard-metrics');
let metricsList = form.querySelector('#metrics-list')
let scorecardDescription = form.querySelector('#scorecard-description');
let charCount = form.querySelector('.counter');
let errorMsgs = form.querySelectorAll('.error-msg')

let createBtn = form.querySelector('#create-btn');

let tagsUl = form.querySelector('.tags-box ul');
let tagsBoxLi = form.querySelectorAll('.tags-box li');
let tagsInput = tagsUl.querySelector('input');

let counter = 0;
let tags = [];
let tagsCancel = [];
let metrics = [];


tagsBoxLi.forEach(li => {
    tags.push(li.textContent);
})


scorecardDescription.addEventListener('keydown', (e) => {
    counter = e.target.value.length
    if (e.key === 'Backspace' && counter > 0) {
        counter -= 1;
    }
    charCount.textContent = counter;
    console.log('keyup')
});

function createTag(tags){
    tagsUl.querySelectorAll('li').forEach(li => li.remove());
    tags.forEach(tag => {
        let tagLi = `<li>${tag} <i class="tag-cancel fa fa-times"></i></li>`;
        tagsInput.insertAdjacentHTML('beforebegin', tagLi);
    })
}

function addTag (e){
    if(e.key === 'Enter' || e.charKey === ','){
        let tag = e.target.value.replace(/\s+/g, ' ');
        if (tag.length > 1){
            tag.split(',').forEach(tag => {
                if( !tags.includes(tag)){
                    tags.push(tag);
                    createTag(tags);
                    tagsInput.value = '';
                    tagsCancel.push(tagsUl.querySelectorAll('li i.tag-cancel'));
                }
            });
        }
    }
}

function removeTag(e){
    console.log(e.target)
}

tagsInput.addEventListener('keyup', addTag);
tagsCancel.forEach(cancel => {cancel.addEventListener('click', removeTag)});
createBtn.addEventListener('click', (e) => e.preventDefault());

metricsSelect.addEventListener('change', (e)=>{
    metrics.push(e.target.value);
    
    let metricLi = `<li>${e.target.value} </li>`;
    metricsList.insertAdjacentHTML('beforebegin', metricLi);
})