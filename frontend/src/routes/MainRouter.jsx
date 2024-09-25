import React from "react";
import { createBrowserRouter, Navigate } from "react-router-dom";

// Metric Pages
import Metrics from '../pages/Metrics';
import MetricCreateEdit from '../pages/MetricCreateEdit';
// Services Pages
import Services from "../pages/Services";
import ServiceCreateEdit from "../pages/ServiceCreateEdit";
import ServiceInfo from "../pages/ServiceInfo";
import ScorecardMetrics from "../pages/ScorecardMetrics";
// NotFound
import NotFound from '../pages/NotFound';

const MainRouter = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/dashboard/services" replace/>
  },
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
      // Service routes
      {
        path: "services",
        element: <Services />,
      },
      {
          path: "services/:service_id",
          element: <ServiceInfo />
      },
      {
          path: "services/:service_id/:scorecard_id",
          element: <ScorecardMetrics />
      },
      {
        path: "services/create",
        element: <ServiceCreateEdit mode="create"/>
      },
      {
        path: "services/edit/:service_id",
        element: <ServiceCreateEdit mode="edit"/>
      }
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
