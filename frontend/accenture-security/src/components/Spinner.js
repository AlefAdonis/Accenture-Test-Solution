/**
 * Loading Component
 *
 * This component displays a circular progress indicator, indicating that content is being loaded.
 *
 * @component
 * @returns {JSX.Element} JSX element representing the Loading component.
 * 
 * @author Álef Ádonis dos Santos Carlos
 */

import * as React from "react";
import CircularProgress from "@mui/material/CircularProgress";
import Box from "@mui/material/Box";

/**
 * Loading Functional Component
 *
 * @returns {JSX.Element} JSX element representing the Loading component.
 */
const Loading = () => {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        marginTop: "10%",
      }}
    >
      <CircularProgress>
        <span className="visually-hidden">Loading...</span>
      </CircularProgress>
    </Box>
  );
};

export default Loading;
