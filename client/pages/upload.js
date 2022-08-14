import React, { useState } from "react";
import Head from "next/head";
import styles from "../styles/Upload.module.css";
import Header from "../components/Header";
import { useRouter } from "next/router";
import { useDropzone, Dropzone } from "react-dropzone";
import { MdOutlineFileUpload } from "react-icons/md";

const Upload = () => {
  const router = useRouter();
  const { acceptedFiles, getRootProps, getInputProps } = useDropzone({
    accept: {
      ".doc": [],
      ".docx": [],
      "application/msword": [],
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        [],
    },
    multiple: false,
  });

  const [file, setFile] = useState(null);

  const files = acceptedFiles.map((file) => setFile(file));

  return (
    <div>
      <Head>
        <title>어플 이름</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        <div className={styles.inputContainer}>
          <section>
            <div className={styles.uploadContainer} {...getRootProps()}>
              <input
                style={{ height: "100%", width: "100%" }}
                {...getInputProps()}
              />
              <MdOutlineFileUpload style={{ height: "3rem", width: "3rem" }} />
              <p style={{ fontWeight: 700 }}>파일 업로드</p>
            </div>
            <aside></aside>
          </section>
        </div>
      </div>
    </div>
  );
};

export default Upload;
