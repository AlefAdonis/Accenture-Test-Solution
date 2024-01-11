/**
 * App Component
 *
 * The main component of the Threats Identifier application.
 *
 * @component
 * @returns {JSX.Element} JSX element representing the App component.
 *
 * @author Álef Ádonis dos Santos Carlos
 */

import { useState, useEffect, useCallback } from "react";
import Header from "./components/Header";
import ExtractionSection from "./components/ExtractionSection";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Loading from "./components/Spinner";
import axios from "axios";
import LogTable from "./components/LogTable";

// API URL for backend server
const API_URL = process.env.REACT_APP_API_URL || "http://127.0.0.1:8080";

/**
 * App Functional Component
 *
 * @returns {JSX.Element} JSX element representing the App component.
 */
const App = () => {
  const [extractedLog, setExtractedLog] = useState([]);
  const [loading, setLoading] = useState(false);

  /**
   * Retrieves logs from the backend server.
   *
   * @async
   * @function
   * @throws {Error} Throws an error if there is an issue retrieving logs.
   */
  const retrieveLogs = useCallback(async () => {
    try {
      const savedLogs = await getSavedLogs();
      setExtractedLog(savedLogs);
    } catch (error) {
      toast.info("Error retrieving logs");
    }
  }, []);

  useEffect(() => {
    retrieveLogs();
  }, [retrieveLogs]);

  /**
   * Handles the extraction of logs from the backend server.
   *
   * @async
   * @function
   */
  const handleExtraction = async () => {
    try {
      setLoading(true);
      const res = await axios.post(`${API_URL}/logs/extract`);

      if (res.status === 200) {
        setExtractedLog(res.data.data);
        toast.success("Logs Extracted!");
        setLoading(false);
      }

      if (res.status === 404) {
        toast.warn("There was no logs to extract.");
        setLoading(false);
      }

      if (res.status === 500) {
        if (res.data.message.includes("extract")) {
          toast.error(`Error while extracting logs!`);
          setLoading(false);
        } else {
          toast.error(`Error saving logs in the database!`);
          setLoading(false);
        }
      }

      setLoading(false);
    } catch (error) {
      console.log(error);
      toast.error(`It was not possible to perform "Extract Logs" Action`);
      setLoading(false);
    }
  };

  /**
   * Retrieves saved logs from the backend server.
   *
   * @async
   * @function
   * @returns {Array} An array of log records.
   * @throws {Error} Throws an error if there is an issue getting logs.
   */
  async function getSavedLogs() {
    try {
      const res = await axios.get(`${API_URL}/logs`);
      return res.data.data;
    } catch (error) {
      throw new Error("Error getting the Log Files!");
    }
  }

  /**
   * Renders the main application layout with header, extraction section, or
   * log table based on the extracted logs state.
   *
   * @returns {JSX.Element} JSX element representing the main application layout.
   */

  return (
    <div>
      <Header />

      {loading ? (
        <Loading />
      ) : !extractedLog.length ? (
        <ExtractionSection extractionFunction={handleExtraction} />
      ) : (
        <LogTable logs={extractedLog} reloadContent={retrieveLogs} />
      )}

      <ToastContainer
        position="bottom-right"
        theme="dark"
        pauseOnHover={false}
        autoClose={3000}
      />
    </div>
  );
};

export default App;
