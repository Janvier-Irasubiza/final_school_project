import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faArrowRightFromBracket,
  faUser,
} from "@fortawesome/free-solid-svg-icons";
import { Link, Navigate, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";

export const AdminNav = () => {
  const location = useLocation();
  const getItemPath = location.pathname.split("/")[2];
  const [activeItem, setActiveItem] = useState(getItemPath || "");

  const handleItemClick = (itemName: string) => {
    setActiveItem(itemName);
  };

  const signout = () => {
    useEffect(() => {
      axios.post('http://127.0.0.1:8000/api/logout/', {
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      })
      .then((response) => {
        if(response.data.success) {
          localStorage.removeItem('id');
          localStorage.removeItem('token');
          Navigate(response.data.to);
        }
      })
      .catch(() => {
        console.log('An unknown error occurred');
      });
    });
  }

  return (
    <nav className="pdg p-fx t-0 w-full">
      <div className="d-flex justify-content-between align-items-center">
        <div>
          <h2 className="bg-ghw">SCMS</h2>
        </div>
        <div>
          <ul className="nav-links">
            <li>
              <Link
                to="profile"
                className={`${activeItem === "profile" ? "active" : ""}`}
                onClick={() => handleItemClick("profile")}
              >
                <FontAwesomeIcon icon={faUser} className="f-13" /> &nbsp;
                Profile
              </Link>
            </li>
            <li>
              <Link to="/" onClick={signout}>
                Sign Out &nbsp;
                <FontAwesomeIcon icon={faArrowRightFromBracket} />
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};
export default AdminNav;
