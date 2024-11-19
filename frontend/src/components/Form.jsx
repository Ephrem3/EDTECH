import { useState } from 'react';
import  EDTECH from '../EDTECH';
import { useNavigate } from 'react-router-dom';




function Form({ route, service}){
    const [NETID, setNETID] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [firstname, setName] = useState('');
    const [lastname, setLastname] = useState('');  
    const [loading, setLoading] = useState(false);
    const nav = useNavigate();

    const name = service === 'login' ? 'Login' : 'Register';

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            if (service === 'login') {
                const res = await EDTECH.post(route, { NETID, password });
                localStorage.setItem('access_token', res.data.accessToken);
                localStorage.setItem('refresh_token', res.data.refreshToken);
                nav('/');
            }
            else {
                await EDTECH.post(route, { NETID, password, email, firstname, lastname });
                nav('/login');

            }
        }
        catch (err) {
            console.log(err);

        }   
        finally {
            setLoading(false);
        }

    };

    return (
        <div className="form">
            <h1>{name}</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="NETID" value={NETID} onChange={(e) => setNETID(e.target.value)} />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                {service === 'register' && (
                    <>
                        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                        <input type="text" placeholder="First Name" value={firstname} onChange={(e) => setName(e.target.value)} />
                        <input type="text" placeholder="Last Name" value={lastname} onChange={(e) => setLastname(e.target.value)} />
                    </>
                )}
                <button type="submit" disabled={loading}>{name}</button>
            </form>
        </div>
        );

}

export default Form;
