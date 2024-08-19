
let form = document.querySelector('form');
let scorecardName = form.querySelector('#scorecard-name');
let scorecardType = form.querySelector('#scorecard-type');
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
    console.log(e.target)
}

let formData = {
    fields: [
        {
            name: 'scorecard-name',
            value: scorecardName.value
        },
        {
            name: 'scorecard-type',
            value: scorecardType.value
        },
        {
            name: 'scorecard-tags',
            value: tags
        },
        {
            name: 'scorecard-description',
            value: scorecardDescription.value
        }
    ]
}

function fetchData(){
    fetch('http://127.0.0.1:8000/api/v1/scorecards', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(user => console.log(user));
}
alert('hi')

tagsInput.addEventListener('keyup', addTag);
tagsCancel.forEach(cancel => {cancel.addEventListener('click', removeTag)});
createBtn.addEventListener('click', fetchData);