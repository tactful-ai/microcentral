import React from "react";
import { createBrowserRouter } from "react-router-dom";

// All Pages
import Services from '../pages/Services.jsx';
import ServiceInfo from '../pages/ServiceInfo.jsx';
import ServiceCreateEdit from '../pages/ServiceCreateEdit';
import ScorecardMetrics from '../pages/ScorecardMetrics';
import Metrics from '../pages/Metrics';
import MetricCreateEdit from '../pages/MetricCreateEdit';
import Scorecards from '../pages/Scorecards';
import ScorecardCreateEdit from '../pages/ScorecardCreateEdit.jsx';
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
            },
            // Scorecards routes
            {
              path: "scorecards",
              element: <Scorecards />
            },
            {
              path: "scorecards/create",
              element: <ScorecardCreateEdit mode="create"/>
            },
            {
              path: "scorecards/edit/:scorecard_id",
              element: <ScorecardCreateEdit mode="edit"/>
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
