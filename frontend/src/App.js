import React from 'react';
import { RouterProvider } from 'react-router-dom';
import ServiceRouter from './routes/ServiceRouter';

function App() {
  return (
    <React.StrictMode>
      <RouterProvider router={ServiceRouter}/>
    </React.StrictMode>
  );
}

export default App;
