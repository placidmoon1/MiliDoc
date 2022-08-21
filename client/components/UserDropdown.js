import styles from "../styles/components/UserDropdown.module.css";
import { Avatar } from "@chakra-ui/react";
import { useRouter } from "next/router";
import { RiArrowDropDownLine } from "react-icons/ri";
import { useState } from "react";
import { Menu, MenuButton, MenuList, MenuItem } from "@chakra-ui/react";

const UserDropdown = (props) => {
  const router = useRouter();
  const [isLoading, setIsLoading] = useState(true);

  const logout = () => {
    axios({
      method: "get",
      url: process.env.NEXT_PUBLIC_API_ROUTE + "auth/logout",
    });
  };

  return (
    <div>
      <Menu>
        <MenuButton>
          <div className={styles.dropdownContainer}>
            {" "}
            <Avatar
              //   src={userData && userData.profile.avatar_url}
              style={{
                height: "2.25rem",
                width: "2.25rem",
              }}
            />
            <RiArrowDropDownLine style={{ fontSize: "1.5rem" }} />
          </div>
        </MenuButton>
        <MenuList>
          <MenuItem onClick={logout}>로그아웃</MenuItem>
        </MenuList>
      </Menu>
    </div>
  );
};

export default UserDropdown;
