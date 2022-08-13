import Head from "next/head";
import styles from "../styles/Home.module.css";
import { Formik, Form, Field } from "formik";
import { Textarea, Button, FormControl } from "@chakra-ui/react";
import Header from "../components/Header";
import { useRouter } from "next/router";
import axios from "axios";

export default function Home() {
  const router = useRouter();
  return (
    <div>
      <Head>
        <title>MiliDoc</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        <div className={styles.inputContainer}>
        <h2>Placeholder text to explain what is happening</h2>
        <br />
          <Formik
            initialValues={{ body: "" }}
            onSubmit={(values, actions) => {
              var bodyFormData = new FormData();
              bodyFormData.append("text", values.body);
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
      </div>
    </div>
  );
}
