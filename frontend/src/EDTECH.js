import axios from 'axios';
import { access_Token } from './constants';

const EDTECH = axios.create({ baseURL: 'http://localhost:8000' });

EDTECH.interceptors.request.use((config) => {
    const token = localStorage.getItem(access_Token);
    if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
},
    (error) => {
        return Promise.reject(error);
    }

);

export default EDTECH;