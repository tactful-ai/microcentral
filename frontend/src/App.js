import React from 'react';
import { RouterProvider } from 'react-router-dom';
import MainRouter from './routes/MainRouter';
import ServiceRouter from './routes/ServiceRouter';

function App() {
  return (
    <React.StrictMode>
      <RouterProvider router={MainRouter}/>
      <RouterProvider router={ServiceRouter}/>
    </React.StrictMode>
  );
}

export default App;
