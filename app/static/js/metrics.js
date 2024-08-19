
let form = document.querySelector('form');
let metricName = form.querySelector('#metric-name');
let metricType = form.querySelector('#metric-type');
let metricDescription = form.querySelector('#metric-description');
let charCount = form.querySelector('.counter');
let errorMsgs = form.querySelectorAll('.error-msg')

let createBtn = form.querySelector('#create-btn');

let tagsUl = form.querySelector('.tags-box ul');
let tagsBoxLi = form.querySelectorAll('.tags-box li');
let tagsInput = tagsUl.querySelector('input');

let charLimit = 5;
let counter = 0;
let tags = [];
let tagsCancel = [];


tagsBoxLi.forEach(li => {
    tags.push(li.textContent);
})



metricDescription.addEventListener('keydown', (e) => {
    counter = e.target.value.length
    if (e.key === 'Backspace' && counter > 0) {
        counter -= 1;
    }
    charCount.textContent = counter;
    console.log('keyup')
});

function createTag(){
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
                    createTag();
                    tagsInput.value = '';
                    tagsCancel.push(tagsUl.querySelectorAll('li i.tag-cancel'));
                    console.log(tagsCancel)
                }
            });
        }
    }
}

function removeTag(e){
    console.log('--canceled--')
}

let formData = {
    fields: [
        {
            name: 'metric-name',
            value: metricName.value
        },
        {
            name: 'metric-type',
            value: metricType.value
        },
        {
            name: 'metric-tags',
            value: tags
        },
        {
            name: 'metric-description',
            value: metricDescription.value
        }
    ]
}


function postData(){
    fetch('http://127.0.0.1:8000/api/v1/metrics', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(user => console.log(user));
}


tagsInput.addEventListener('keyup', addTag);
tagsCancel.forEach(cancel => {cancel.addEventListener('click', removeTag)});
createBtn.addEventListener('click', postData);