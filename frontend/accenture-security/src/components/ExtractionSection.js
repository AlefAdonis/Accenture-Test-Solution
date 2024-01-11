/**
 * ExtractionSection Component
 *
 * This component represents a section for handling log extraction.
 *
 * @component
 * @param {Object} props - The properties passed to the component.
 * @param {Function} props.extractionFunction - The function to be executed when the "Extract Log Files" button is clicked.
 *
 * @example
 * // Example usage of ExtractionSection component:
 * <ExtractionSection extractionFunction={handleExtraction} />
 * 
 * @author Álef Ádonis dos Santos Carlos
 */

import React from "react";
import Container from "react-bootstrap/Container";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";


/**
 * ExtractionSection Functional Component
 *
 * @param {Object} props - The properties passed to the component.
 * @param {Function} props.extractionFunction - The function to be executed when the "Extract Log Files" button is clicked.
 *
 * @returns {JSX.Element} JSX element representing the ExtractionSection component.
 */
const ExtractionSection = ({ extractionFunction }) => {
  return (
    <Container
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        marginTop: "10%"
      }}
    >
      <Box
        sx={{
          justifyContent: "center",
          display: "flex",
          flexWrap: "wrap",
          "& > :not(style)": {
            m: 1,
            width: "100%",
            padding: "10px",
            height: 100,
          },
        }}
      >
        <Paper elevation={3}>
          <Container
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              height: "100%",
            }}
          >
            It appears that there is no Logs Extracted. Do you want to extract
            the files?
          </Container>
        </Paper>
      </Box>
      <Button
        variant="contained"
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          height: "100%",
          width: "20%"
        }}
        onClick={() => extractionFunction()}
      >
        Extract Log FIles
      </Button>
    </Container>
  );
};

export default ExtractionSection;
