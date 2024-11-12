import { usestate } from 'react';
import  EDTECH from '../EDTECH';
import { useNavigate } from 'react-router-dom';




function Form({ route, service}){
    const [NETID, setNETID] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [firstname, setName] = useState('');
    const [lastname, setLastname] = useState('');   
    const nav = useNavigate();

    const name = service === 'login' ? 'Login' : 'Register';

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await EDTECH.post(route, {
                NETID,
                password,
                email,
                firstname,
                lastname    
            });

        }
    }

}
