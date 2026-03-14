/**
 * PECH Platform Tools — Google Apps Script
 * Project: PECH Tech Education Tracker
 *
 * FIX NOTES (2026-03-14):
 * - The "An unknown error has occurred" was caused by:
 *   1. Missing error handling — if the sheet has no data or wrong structure, it crashes
 *   2. No null/undefined checks on data array access
 *   3. Possible timeout on large datasets
 *   4. Using SpreadsheetApp.getUi().alert() which only works from menu-triggered functions
 *
 * SOLUTION: Added proper error handling, data validation, and try-catch blocks.
 */

// ============================================================
// MENU SETUP — Must run from a container-bound script
// ============================================================
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('PECH Tools')
    .addItem('Setup Sheets', 'setupSheets')
    .addItem('Generate Education Report', 'generateEducationReport')
    .addSeparator()
    .addItem('Refresh Data', 'refreshData')
    .addToUi();
}

// ============================================================
// SETUP SHEETS — Creates required sheet structure
// ============================================================
function setupSheets() {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    if (!ss) {
      throw new Error('This script must be run from within a Google Spreadsheet.');
    }

    // Check if "Tech Education" sheet exists, create if not
    var sheet = ss.getSheetByName('Tech Education');
    if (!sheet) {
      sheet = ss.insertSheet('Tech Education');

      // Set up headers
      var headers = [
        'Student Name',
        'Email',
        'Course',
        'Start Date',
        'Status',
        'Progress (%)',
        'Completion Date',
        'Certificate Issued'
      ];

      sheet.getRange(1, 1, 1, headers.length).setValues([headers]);

      // Format headers
      var headerRange = sheet.getRange(1, 1, 1, headers.length);
      headerRange.setBackground('#00BFFF');
      headerRange.setFontColor('#FFFFFF');
      headerRange.setFontWeight('bold');

      // Set column widths
      sheet.setColumnWidth(1, 200); // Student Name
      sheet.setColumnWidth(2, 250); // Email
      sheet.setColumnWidth(3, 200); // Course
      sheet.setColumnWidth(4, 120); // Start Date
      sheet.setColumnWidth(5, 100); // Status
      sheet.setColumnWidth(6, 100); // Progress
      sheet.setColumnWidth(7, 120); // Completion Date
      sheet.setColumnWidth(8, 130); // Certificate

      // Add sample data
      var sampleData = [
        ['John Doe', 'john@example.com', 'Solar Installation 101', '2026-01-15', 'In Progress', 75, '', 'No'],
        ['Jane Smith', 'jane@example.com', 'IoT Fundamentals', '2026-01-10', 'Completed', 100, '2026-03-01', 'Yes'],
        ['Ahmed Hassan', 'ahmed@example.com', 'Electrical Wiring', '2026-02-01', 'In Progress', 45, '', 'No']
      ];

      sheet.getRange(2, 1, sampleData.length, sampleData[0].length).setValues(sampleData);

      SpreadsheetApp.getUi().alert(
        'PECH Tech Education Sheet Created\n\n' +
        'Headers and sample data have been added.\n' +
        'You can now add student records and run the Education Report.'
      );
    } else {
      SpreadsheetApp.getUi().alert(
        'Sheet "Tech Education" already exists.\n' +
        'Use "Generate Education Report" to view statistics.'
      );
    }

  } catch (e) {
    Logger.log('setupSheets error: ' + e.message);
    // Use try-catch for UI alert in case it's run from a trigger (not menu)
    try {
      SpreadsheetApp.getUi().alert('Error: ' + e.message);
    } catch (uiError) {
      Logger.log('Cannot show UI alert (probably triggered, not menu-invoked): ' + e.message);
    }
  }
}

// ============================================================
// GENERATE EDUCATION REPORT — Fixed version of the broken function
// ============================================================
function generateEducationReport() {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    if (!ss) {
      throw new Error('This script must be run from within a Google Spreadsheet.');
    }

    var sheet = ss.getSheetByName('Tech Education');
    if (!sheet) {
      SpreadsheetApp.getUi().alert(
        'Error: "Tech Education" sheet not found.\n\n' +
        'Run "Setup Sheets" first from the PECH Tools menu.'
      );
      return;
    }

    var data = sheet.getDataRange().getValues();

    // Validate data structure
    if (!data || data.length <= 1) {
      SpreadsheetApp.getUi().alert(
        'No student data found.\n\n' +
        'Add student records below the header row first.'
      );
      return;
    }

    // Validate we have enough columns (need at least 6 for progress)
    if (data[0].length < 6) {
      SpreadsheetApp.getUi().alert(
        'Sheet structure error: Expected at least 6 columns.\n' +
        'Run "Setup Sheets" to create the correct structure.'
      );
      return;
    }

    var total = data.length - 1; // Exclude header row
    var completed = 0;
    var totalProgress = 0;

    for (var i = 1; i < data.length; i++) {
      var progress = Number(data[i][5]); // Column F = Progress (%)

      // Validate progress is a number
      if (!isNaN(progress)) {
        totalProgress += progress;
        if (progress >= 100) {
          completed++;
        }
      }
    }

    var avgProgress = total > 0 ? Math.round(totalProgress / total) : 0;
    var completionRate = total > 0 ? Math.round((completed / total) * 100) : 0;

    SpreadsheetApp.getUi().alert(
      'PECH Tech Education Report\n\n' +
      'Total Students: ' + total + '\n' +
      'Completed: ' + completed + '\n' +
      'In Progress: ' + (total - completed) + '\n' +
      'Average Progress: ' + avgProgress + '%\n' +
      'Completion Rate: ' + completionRate + '%'
    );

  } catch (e) {
    Logger.log('generateEducationReport error: ' + e.message);
    try {
      SpreadsheetApp.getUi().alert('Error generating report: ' + e.message);
    } catch (uiError) {
      Logger.log('UI error: ' + uiError.message);
    }
  }
}

// ============================================================
// REFRESH DATA — Utility function
// ============================================================
function refreshData() {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('Tech Education');

    if (!sheet) {
      SpreadsheetApp.getUi().alert('No "Tech Education" sheet found. Run Setup first.');
      return;
    }

    // Force recalculation
    SpreadsheetApp.flush();

    SpreadsheetApp.getUi().alert('Data refreshed successfully.');

  } catch (e) {
    Logger.log('refreshData error: ' + e.message);
  }
}
