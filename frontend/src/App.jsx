import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import ProtectedRoute from "./components/ProtectedRoute";



function Logout () {
    localStorage.clear();
    return <Navigate to="/login" />;
}

function Home() {
    return (
        <div>
            <h1>Home</h1>
            <button onClick={Logout}>Logout</button>
        </div>
    );
}

    
function App() {
    return (
        <Router>
            <Routes>
                <Route 
                    path="/"
                    element={
                        <ProtectedRoute>
                            <Home />
                        </ProtectedRoute>
                    }
                    />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
               
            </Routes> 
        </Router>
    );

}

export default App;