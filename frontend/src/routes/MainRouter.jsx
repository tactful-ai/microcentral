import React from "react";
import { createBrowserRouter } from "react-router-dom";

// All Pages
import Metrics from '../pages/Metrics';
import MetricCreateEdit from '../pages/MetricCreateEdit';
import NotFound from '../pages/NotFound';

const MainRouter = createBrowserRouter([
  {
    path: "/dashboard",
    children: [
      // Metrics routes
      {
        path: "metrics",
        element: <Metrics />
      },
      {
        path: "metrics/create",
        element: <MetricCreateEdit mode="create"/>
      },
      {
        path: "metrics/edit/:metric_id",
        element: <MetricCreateEdit mode="edit"/>
      },
    ]
  },
  // Not Found
  {
    path: "/404",
    element: <NotFound />
  },
  {
    path: "*",
    element: <NotFound />
  },
]);

export default MainRouter;
