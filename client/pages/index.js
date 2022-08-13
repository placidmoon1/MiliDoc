import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import { Formik, Form, Field } from "formik";
import { Input, Textarea, Button, FormControl } from "@chakra-ui/react";
import ResizeTextarea from "react-textarea-autosize";
import Header from "../components/Header";
import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();
  return (
    <div>
      <Head>
        <title>어플 이름</title>
        {/* <meta name="description" content="Generated by create next app" /> */}
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        <div className={styles.inputContainer}>
          <Formik
            initialValues={{ body: "" }}
            onSubmit={(values, actions) => {
              router.push("/results");
              // axios({
              //   method: "post",
              //   url: process.env.NEXT_PUBLIC_API_ROUTE + "/api/...",
              //   data: JSON.stringify({
              //     body: values.body,
              //   }),
              //   headers: {
              //     "Content-Type": "application/json",
              //   },
              // }).then((res) => {
              //   if (res.status === 201) router.push("/results");
              //   else actions.setSubmitting(false);
              // });
            }}
          >
            {(props) => (
              <Form>
                <Field name="body" validate={console.log("helo")}>
                  {({ field, form }) => (
                    <FormControl
                      isInvalid={form.errors.name && form.touched.name}
                    >
                      <Textarea
                        {...field}
                        id="body"
                        resize="none"
                        style={{ height: "400px", width: "100%", backgroundColor: "white" }}
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
                  {/* <Button
                  variant="solid"
                  style={{marginLeft: "5px"}}
                >
                  다시쓰기
                </Button> */}
                </div>
              </Form>
            )}
          </Formik>
        </div>
      </div>
    </div>
  );
}