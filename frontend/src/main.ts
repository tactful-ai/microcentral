import App from "@/App.vue";
import axios from "axios";
import { createApp } from "vue";
import router from "./router";

import "./assets/main.css";

axios.defaults.baseURL = "http://localhost:8000/api";

axios({
	method: 'get',
	url: '/v1/teams/?skip=0&limit=100'
	
}).then(function (response) {
	console.log(response);
}).catch(function (error) {
	console.log(error);
});

const app = createApp(App);

app.use(router);

app.mount("#app");
