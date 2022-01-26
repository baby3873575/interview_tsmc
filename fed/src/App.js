import React, { Component } from "react";
import "./App.css";
import Users from "./components/Users";

export default class App extends Component {
  state = {
    users: [],
    showDone: false
  };

  handleDone = user => {
    alert("not implemented yet")
    const users = [...this.state.users];
    const index = users.indexOf(user);

  };

  

  handleMoreDetail = user => {
    const users = [...this.state.users];
    const index = users.indexOf(user);
    fetch("/api/v1/user/" + user.id)
      .then(response => response.json())
      .then(data => {
        users[index] = data;
        this.setState({ users });
      })
      .catch(error => console.log(error));
  };

  handleViewToggle = bool => this.setState({ showDone: bool });

  usersSelector = () => {
    return this.state.users;
  };

  componentDidMount() {
    fetch("/api/v1/users")
      .then(response => response.json())
      .then(data => this.setState({ users: data }))
      .catch(error => console.log(error));
  }

  render() {
    return (
      <div className="container-fluid mt-5">
      
        <div className="row justify-content-center">
          <div className="col-8">
            <div className="card text-center">
            <h1>Users Board</h1>
              {/* <div className="card-header">
                <ul className="nav card-header-pills justify-content-center">
                  <li className="nav-item">
                    <ViewToggle
                      handleViewToggle={this.handleViewToggle}
                      showDone={this.state.showDone}
                    />
                  </li>
                </ul>
              </div> */}
              <Users
                users={this.usersSelector()}
                handleDone={this.handleDone}
                handleMoreDetail={this.handleMoreDetail}
              />
            </div>
          </div>
        </div>
      </div>
    );
  }
}
