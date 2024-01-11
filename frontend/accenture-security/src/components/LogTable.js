/**
 * LogTable Component
 *
 * This component displays a table of log records using the MUI DataGrid.
 *
 * @component
 * @param {Object} props - The properties passed to the component.
 * @param {Array} props.logs - An array of log records to be displayed in the table.
 * @param {Function} props.reloadContent - The function to reload the content when the reload button is clicked.
 *
 * @example
 * // Example usage of LogTable component:
 * <LogTable logs={logData} reloadContent={handleReload} />
 * 
 * @author Álef Ádonis dos Santos Carlos
 */

import React from "react";
import { Box, Typography } from "@mui/material";
import { DataGrid, gridClasses } from "@mui/x-data-grid";
import Button from "@mui/material/Button";
import CachedIcon from "@mui/icons-material/Cached";

// Columns configuration for the log table
const logColumns = [
  { field: "log_id", headerName: "Log ID", width: 120 },
  {
    field: "date",
    headerName: "Date",
    width: 120,
    valueGetter: (params) => {
      const dateString = params.row.date;
      const dateObject = new Date(dateString);

      const formattedDate = dateObject.toLocaleDateString("en-US");

      return formattedDate;
    },
  },
  { field: "hour", headerName: "Hour", width: 120 },
  { field: "software_name", headerName: "Software Name", width: 150 },
  { field: "version", headerName: "Version", width: 100 },
  { field: "title", headerName: "Title", width: 200 },
  { field: "ip_address", headerName: "IP Address", width: 150 },
  { field: "description", headerName: "Description", width: 300 },
  { field: "id", headerName: "ID", width: 70 },
  { field: "origin_file", headerName: "Origin File", width: 150 },
];

/**
 * LogTable Functional Component
 *
 * @param {Object} props - The properties passed to the component.
 * @param {Array} props.logs - An array of log records to be displayed in the table.
 * @param {Function} props.reloadContent - The function to reload the content when the reload button is clicked.
 *
 * @returns {JSX.Element} JSX element representing the LogTable component.
 */
const LogTable = ({ logs, reloadContent }) => {
  return (
    <Box
      sx={{
        height: 500,
        width: "100%",
        marginLeft: "90%%",
        marginTop: 5,
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          marginBottom: "20px",
        }}
      >
        <Typography variant="h4" component="h4" sx={{ fontSize: 26 }}>
          Log Records
        </Typography>

        <div style={{ marginLeft: "auto" }}>
          <Button
            variant="outlined"
            style={{
              height: "32px",
              width: "32px",
            }}
            title="Reload the Dashboard"
            onClick={() => reloadContent()}
          >
            <CachedIcon />
          </Button>
        </div>
      </div>
      
      {/* MUI DataGrid component for rendering the log records */}
      <DataGrid
        columns={logColumns}
        rows={logs}
        getRowId={(row) => row.id}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 20 },
          },
        }}
        pageSizeOptions={[5, 10, 20]}
        getRowHeight={() => "auto"}
        getRowSpacing={(params) => ({
          top: params.isFirstVisible ? 0 : 5,
          bottom: params.isLastVisible ? 0 : 5,
        })}
        sx={{
          [`& .${gridClasses.row}`]: {
            bgcolor: "#EEEEEE",
          },
        }}
        slotProps={{ toolbar: { showQuickFilter: true } }}
      />
    </Box>
  );
};

export default LogTable;
