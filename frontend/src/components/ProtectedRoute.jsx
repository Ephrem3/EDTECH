import { Navigate } from "react-router-dom";
import { jwtDecode }  from 'jwt-decode';
import EDTECH from '../EDTECH';
import { useState } from "react";
import { useEffect } from "react";





const ProtectedRoute = ({ element }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);


    useEffect(() => {

        checkAuth(); }, []);

        const refreshToken = async () => {
            const refreshToken = localStorage.getItem('refresh_token');
            try {
                const res = await EDTECH.post('token/refresh', { refreshToken: refreshToken });
                if (res.status === 200) {
                    localStorage.setItem('access_token', res.data.accessToken);
                    localStorage.setItem('refresh_token', res.data.refreshToken);
                    setIsAuthenticated(true);
                }
                else {
                    setIsAuthenticated(false);
                }
            }
            catch (err) {
                console.log(err);
                setIsAuthenticated(false);
            }


        };

        const checkAuth = async () => {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    return setIsAuthenticated(false);
                }

                const decode = jwtDecode(token);
                const currentTime = Date.now() / 1000;
                const isTokenValid = decode.exp > currentTime;


                isTokenValid ? setIsAuthenticated(true) : await refreshToken();
  
        };

        if (isAuthenticated === null) {
            return <div>Loading...</div>;     
        }

       return isAuthenticated ? element : <Navigate to="/login" />;
       

    };

    export default ProtectedRoute;