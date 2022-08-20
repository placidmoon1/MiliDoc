import { useState } from "react";
import Head from "next/head";
import styles from "../styles/Login.module.css";
import Header from "../components/Header";
import { Formik, Form, Field } from "formik";
import { Button, FormControl, Input } from "@chakra-ui/react";
import { useRouter } from "next/router";
import axios from "axios";
import Image from "next/image";

const Login = () => {
  const router = useRouter();
  const [isError, setIsError] = useState(false);

  return (
    <div>
      <Head>
        <title>로그인 - MiliDoc</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        <div className={styles.inputContainer}>
          <div className={styles.formContainer}>
            <Image src="/logo.png" width={150} height={50} />
            <br />
            <Formik
              initialValues={{ username: "", password: "" }}
              onSubmit={(values, actions) => {
                var bodyFormData = new FormData();
                bodyFormData.append("username", values.username);
                bodyFormData.append("password", values.password);
                console.log("lolololo")
                axios({
                  method: "post",
                  url: process.env.NEXT_PUBLIC_API_ROUTE + "auth/login",
                  data: bodyFormData,
                  headers: {
                    "Content-Type": "multipart/form-data",
                  },
                }).then((res) => {
                  console.log("hello")
                  console.log(res);
                  if (res.status === 200) {
                    axios({
                      method: "get",
                      url: process.env.NEXT_PUBLIC_API_ROUTE + "auth/getemail",
                    }).then((res) => {
                      console.log(res);
                    });
                    router.push("/");
                  } else {
                    setIsError(true);
                  }
                });
                actions.setSubmitting(false);
              }}
            >
              {(props) => (
                <Form>
                  <Field name="username">
                    {({ field, form }) => (
                      <FormControl>
                        <div className={styles.fieldTextContainer}>
                          <h2>이메일</h2>
                          <h3>*</h3>
                        </div>
                        <Input {...field} id="username" />
                      </FormControl>
                    )}
                  </Field>
                  <br />
                  <Field name="password">
                    {({ field, form }) => (
                      <FormControl>
                        <div className={styles.fieldTextContainer}>
                          <h2>비밀번호</h2>
                          <h3>*</h3>
                        </div>
                        <Input {...field} id="password" type="password" />
                      </FormControl>
                    )}
                  </Field>
                  <br />
                  {isError ? (
                    <p style={{ fontSize: "0.75rem", color: "red" }}>
                      이메일 아니면 비밀번호가 틀렸습니다.
                    </p>
                  ) : (
                    ""
                  )}
                  <div className={styles.buttonContainer}>
                    <Button
                      variant="solid"
                      isDisabled={
                        props.values.username === "" ||
                        props.values.password === ""
                      }
                      isLoading={props.isSubmitting}
                      type="submit"
                      style={{ width: "100%" }}
                    >
                      로그인
                    </Button>
                  </div>
                </Form>
              )}
            </Formik>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
