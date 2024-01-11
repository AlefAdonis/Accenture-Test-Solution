/**
 * Header Component
 *
 * This component represents the header section of the Threats Identifier application.
 *
 * @component
 * @returns {JSX.Element} JSX element representing the Header component.
 * 
 * @author Álef Ádonis dos Santos Carlos
 */

import React from "react";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import SecurityIcon from "@mui/icons-material/Security";

// Styles for the header container, title, and icon
const headerContainerStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const titleStyle = {
  fontSize: "36px",
  marginLeft: "10px",
};

const iconStyle = {
  fontSize: "32px",
};

/**
 * Header Functional Component
 *
 * @returns {JSX.Element} JSX element representing the Header component.
 */
const Header = () => {
  return (
    <Navbar className="mt-1">
      <Container style={headerContainerStyle}>
        <SecurityIcon style={iconStyle} />
        <div style={titleStyle}>Threats Identifier</div>
      </Container>
    </Navbar>
  );
};

export default Header;
