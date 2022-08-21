import React, { useState } from "react";
import Head from "next/head";
import styles from "../../styles/Search.module.css";
import Header from "../../components/Header";
import { useRouter } from "next/router";
import {
  Input,
  InputGroup,
  InputLeftElement,
  RadioGroup,
  Radio,
  Stack,
} from "@chakra-ui/react";
import { MdSearch } from "react-icons/md";

const Search = () => {
    const router = useRouter();

  const [value, setValue] = useState("");
  const [searchLanguage, setSearchLanguage] = useState("ko");

  const searchValue = () => {
    router.push({ pathname: "/search/result", query: { q: value, l: searchLanguage } });
    return;
  };

  return (
    <div>
      <Head>
        <title>MiliDoc</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        <div className={styles.inputContainer}>
          <div style={{ marginBottom: "10px" }}>
            <h2>군사 용어 사전</h2>
          </div>
          <form
            onSubmit={(e) => {
              e.preventDefault();
              searchValue();
            }}
          >
            <InputGroup>
              <InputLeftElement
                onClick={(e) => {
                  e.preventDefault();
                  searchValue();
                }}
                style={{ height: "100%" }}
                pointerEvents="none"
                children={
                  <button type="submit">
                    <MdSearch
                      style={{
                        marginLeft: "6px",
                        height: "24px",
                        width: "24px",
                      }}
                    />
                  </button>
                }
              />
              <Input
                value={value}
                onChange={(e) => setValue(e.currentTarget.value)}
                size="lg"
              />
            </InputGroup>
          </form>
          <div style={{ marginTop: "15px" }}>
            <RadioGroup onChange={setSearchLanguage} value={searchLanguage}>
              <Stack direction="row">
                <Radio value="ko">한국어</Radio>
                <Radio value="en">영어</Radio>
              </Stack>
            </RadioGroup>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Search;
