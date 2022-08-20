import { useState, useEffect } from "react";
import Head from "next/head";
import styles from "../styles/Signup.module.css";
import Header from "../components/Header";
import { Formik, Form, Field } from "formik";
import { Textarea, Button, FormControl, Input } from "@chakra-ui/react";
import { useRouter } from "next/router";
import axios from "axios";
import Image from "next/image";

const Signup = () => {
  const router = useRouter();
  return (
    <div>
      <Head>
        <title>회원가입 - MiliDoc</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        <div className={styles.inputContainer}>
          <div className={styles.formContainer}>
            <Image src="/logo.png" width={150} height={50} />
            <br />
            <Formik
              initialValues={{
                code: "",
                username: "",
                password: "",
                passwordConfirmation: "",
              }}
              onSubmit={(values, actions) => {
                var bodyFormData = new FormData();
                bodyFormData.append("username", values.username);
                bodyFormData.append("password", values.password);
                bodyFormData.append("secret_status", values.code);
                axios({
                  method: "post",
                  url: process.env.NEXT_PUBLIC_API_ROUTE + "auth/register",
                  data: bodyFormData,
                  headers: {
                    "Content-Type": "multipart/form-data",
                  },
                }).then((res) => {
                  if (res.status === 200) {
                    var bodyFormData = new FormData();
                    bodyFormData.append("username", values.username);
                    bodyFormData.append("password", values.password);
                    axios({
                      method: "post",
                      url: process.env.NEXT_PUBLIC_API_ROUTE + "auth/login",
                      data: bodyFormData,
                      headers: {
                        "Content-Type": "multipart/form-data",
                      },
                    }).then((res) => {
                      console.log(res);
                      if (res.status === 200) router.push("/");
                    });
                  }
                });
                actions.setSubmitting(false);
              }}
            >
              {(props) => (
                <Form>
                  <Field name="code">
                    {({ field, form }) => (
                      <FormControl>
                      <div className={styles.fieldTextContainer}>
                          <h2>소속코드</h2>
                          <h3>*</h3>
                        </div>
                        <Input {...field} id="code" />
                      </FormControl>
                    )}
                  </Field>
                  <hr />
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
                  <hr />
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
                  {props.values.password ===
                  props.values.passwordConfirmation ? (
                    <p style={{ marginTop: "10px" }}></p>
                  ) : (
                    <p
                      style={{
                        fontSize: "10px",
                        marginTop: "5px",
                        color: "red",
                      }}
                    >
                      비밀번호가 틀렸습니다.
                    </p>
                  )}
                  <hr />
                  <Field name="passwordConfirmation">
                    {({ field, form }) => (
                      <FormControl>
                        <div className={styles.fieldTextContainer}>
                          <h2>비밀번호 재확인</h2>
                          <h3>*</h3>
                        </div>
                        <Input
                          {...field}
                          id="passwordConfirmation"
                          type="password"
                        />
                      </FormControl>
                    )}
                  </Field>
                  <br />
                  <div className={styles.buttonContainer}>
                    <Button
                      variant="solid"
                      isDisabled={
                        props.values.username === "" ||
                        props.values.password === "" ||
                        props.values.password !==
                          props.values.passwordConfirmation
                      }
                      isLoading={props.isSubmitting}
                      type="submit"
                      style={{ width: "100%" }}
                    >
                      회원가입
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

export default Signup;
