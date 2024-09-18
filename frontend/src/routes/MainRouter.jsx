import React from "react";
import { createBrowserRouter } from "react-router-dom";

// All Pages
import Services from '../pages/Services.jsx';
import Metrics from '../pages/Metrics';
import MetricCreateEdit from '../pages/MetricCreateEdit';
import Scorecards from '../pages/Scorecards';
import NotFound from '../pages/NotFound';

const MainRouter = createBrowserRouter([
    // Services routes
    {
      path: "/",
      element: <Services />
    },
    {
        path: "/dashboard",
        children: [
            {
                path: "services",
                element: <Services />,
            },
            // Scorecards routes
            {
              path: "scorecards",
              element: <Scorecards />
            },
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
