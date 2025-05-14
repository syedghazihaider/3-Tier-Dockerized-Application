import React, { useState, useEffect } from "react";

// Main component
function App() {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({ name: "", age: "" });

  // Fetch all users from backend
  const fetchUsers = async () => {
    try {
      const response = await fetch("http://localhost:5000/users");
      const data = await response.json();
      setUsers(data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  // Add a new user
  const addUser = async (e) => {
    e.preventDefault();

    if (!newUser.name || !newUser.age) {
      alert("Please provide both name and age");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/add", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(newUser)
      });

      const data = await response.json();

      // Update the list of users with the new user
      setUsers([...users, data]);
      setNewUser({ name: "", age: "" }); // Clear input fields
    } catch (error) {
      console.error("Error adding user:", error);
    }
  };

  useEffect(() => {
    fetchUsers(); // Fetch users on initial load
  }, []);

  return (
    <div className="App">
      <h1>User List</h1>
      
      <div>
        <h2>Add a New User</h2>
        <form onSubmit={addUser}>
          <input
            type="text"
            placeholder="Name"
            value={newUser.name}
            onChange={(e) => setNewUser({ ...newUser, name: e.target.value })}
          />
          <input
            type="number"
            placeholder="Age"
            value={newUser.age}
            onChange={(e) => setNewUser({ ...newUser, age: e.target.value })}
          />
          <button type="submit">Add User</button>
        </form>
      </div>

      <h2>All Users</h2>
      <ul>
        {users.length === 0 ? (
          <li>No users found</li>
        ) : (
          users.map((user) => (
            <li key={user.id}>
              {user.name} ({user.age} years old)
            </li>
          ))
        )}
      </ul>
    </div>
  );
}

export default App;
