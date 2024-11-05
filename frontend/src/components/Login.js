import axios from 'axios';
import React, { useState } from 'react';

export const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    
    const submit = async e => {
        e.preventDefault();
        const user = { username: username,
                        password: password
                    };
                    
        const {data} = await axios.post('http://localhost:8000/token/', user ,{headers:
        {
            'Content-Type': 'application/json'}},
            {withCredentials: true});
        localStorage.clear();
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);    
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + data.access;
        window.location.href = '/';
    }



    return (
        <div>
            <h1>Login</h1>
            <input type="username" placeholder="username" onChange={(e) => setUsername(e.target.value)} />
            <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
            <button onClick={submit}>Login</button>
            <h3>{message}</h3>
        </div>
    )
}
