import React from "react";
import { createBrowserRouter } from "react-router-dom";

// All Pages
import Scorecards from '../pages/Scorecards';
import ScorecardCreateEdit from '../pages/ScorecardCreateEdit.jsx';
import NotFound from '../pages/NotFound';

const MainRouter = createBrowserRouter([
    {
        path: "/dashboard",
        children: [
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
