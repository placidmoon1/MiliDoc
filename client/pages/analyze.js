import Head from "next/head";
import styles from "../styles/Analyze.module.css";
import { Formik, Form, Field } from "formik";
import { Textarea, Button, FormControl } from "@chakra-ui/react";
import Header from "../components/Header";
import { useRouter } from "next/router";
import axios from "axios";

import { useState } from "react";

export default function Analyze() {
  const [isLoading, setIsLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [originalText, setOriginalText] = useState("");

  const reset = () => {
    setOriginalText("");
    setSubmitted(false);
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
        {submitted ? (
          <div className={styles.resultContainer}>
            <p>{originalText}</p>
            <div className={styles.buttonContainer}>
              <Button onClick={reset} variant="solid" style={{marginTop: "1rem"}}>
                다시하기
              </Button>
            </div>
          </div>
        ) : (
          <div className={styles.inputContainer}>
            <h2 style={{ fontWeight: 600, fontSize: "1.5rem" }}>
              금칙어 및 등등을 MiliDoc에서 검사를 하십쇼!
            </h2>
            <br />
            <Formik
              initialValues={{ body: "" }}
              onSubmit={(values, actions) => {
                setIsLoading(true);
                var bodyFormData = new FormData();
                bodyFormData.append("text", values.body);
                setOriginalText(values.body);
                axios({
                  method: "post",
                  url: process.env.NEXT_PUBLIC_API_ROUTE + "check/text",
                  data: bodyFormData,
                  headers: {
                    "Content-Type": "multipart/form-data",
                  },
                }).then((res) => {
                  console.log(res);
                  // if (res.status === 201) router.push("/results");
                  // else actions.setSubmitting(false);
                });
                setIsLoading(false);
                setSubmitted(true);
                actions.setSubmitting(false);
              }}
            >
              {(props) => (
                <Form>
                  <Field name="body">
                    {({ field, form }) => (
                      <FormControl>
                        <Textarea
                          {...field}
                          id="body"
                          resize="none"
                          style={{
                            height: "400px",
                            width: "100%",
                            backgroundColor: "white",
                          }}
                        />
                      </FormControl>
                    )}
                  </Field>
                  <div className={styles.buttonContainer}>
                    <Button
                      variant="solid"
                      isDisabled={props.values.body === ""}
                      isLoading={props.isSubmitting}
                      type="submit"
                    >
                      검사하기
                    </Button>
                  </div>
                </Form>
              )}
            </Formik>
          </div>
        )}
      </div>
    </div>
  );
}
