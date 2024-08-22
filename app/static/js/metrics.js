
const form = document.querySelector('form');
const metricName = form.querySelector('#metric-name');
const metricType = form.querySelector('#metric-type');
const metricTypeOptions = metricType.querySelectorAll('option');
const metricDescription = form.querySelector('#metric-description');
const charCount = form.querySelector('.counter');
const errorMsgs = form.querySelectorAll('.error-msg')

const createBtn = form.querySelector('#create-btn');

const tagsUl = form.querySelector('.tags-box ul');
const tagsBoxLi = form.querySelectorAll('.tags-box li');
const tagsInput = tagsUl.querySelector('input');

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
});

function createTag(tags = []){
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
                    // console.log(tagsCancel)
                }
            });
        }
    }
}

function removeTag(e){
    console.log(e.target)
}


function PostMetric(e){
    e.preventDefault();
    
    let formData = {
        name: metricName.value,
        type: metricType.options[metricType.selectedIndex].text,
        area: tags,
        description: metricDescription.value
    }

    const response = async () => {
        var data = await fetch('http://127.0.0.1:8000/api/v1/metrics', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then((response) => response.json())
        var responseData = {
            message: data.message,
            object: data.object
        }
        console.log(responseData)
    };
    response();
}

const formMode = form.dataset.mode;
if(formMode == 'edit'){
    const pathname = window.location.pathname;
    const regex = /(\d+)$/;
    const metric_id = pathname.match(regex)[0];
    const request = async () => {
        var data = await fetch(`http://127.0.0.1:8000/api/v1/metrics/${metric_id}`)
        .then((response) => response.json());
        
        var metric_data = data.object;
        console.log(metric_data)

        metricName.value = metric_data.name;
        metricDescription.value = metric_data.description;

        metric_data.area.forEach(area => {
            tags.push(area)
        })
        createTag(metric_data.area)

        metricType.value = metric_data.type
        
        metricTypeOptions.forEach(option => {
            if(option.text == metric_data.type){
                option.selected = true;
            }
        })
    };
    request('PromiseResult');
}

console.log('hi2')


tagsInput.addEventListener('keyup', addTag);
tagsCancel.forEach(cancel => {cancel.addEventListener('click', removeTag)});
createBtn.addEventListener('click', PostMetric);