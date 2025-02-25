import pandas as pd
import pymssql
# Set up the database connection details
server = '10.0.1.146'
database = 'HRIS'
username = 'db_admin'
password = 'FgiDb@dm1n2017'


try:
    # Establish connection
    conn = pymssql.connect(server, username, password, database)

    # Define the SQL query
    sql_query = """
    SELECT EmployeeCode, EmployeeName, DateOfBirth, DepartmentName
    FROM hr.vw_EmployeeExpanded
    WHERE StatusCode = 'ACTIVE'
    ORDER BY DepartmentName, EmployeeName
    """

    # Execute the SQL query and load results into a DataFrame
    df = pd.read_sql_query(sql_query, conn)

    # Close the database connection
    conn.close()

    # Save DataFrame to Excel file
    excel_filename = 'employee_data.xlsx'
    df.to_excel(excel_filename, index=False)

    print(f"Data saved to '{excel_filename}' successfully.")

except pymssql.Error as e:
    print("Error:", e)

