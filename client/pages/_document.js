import Document, { Html, Head, Main, NextScript } from "next/document";

class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          <meta
            name="description"
            content="당신의 텍스트를 넣어주세요. Milidoc이 당신만의 가이드가 되어줍니다."
          ></meta>
          <meta property="og:type" content="website"></meta>
          <meta
            property="og:title"
            content="MiliDoc (Military Documentation Doctor)"
          ></meta>
          <meta
            property="og:description"
            content="당신의 텍스트를 넣어주세요. Milidoc이 당신만의 가이드가 되어줍니다."
          ></meta>
          <meta
            property="og:image"
            content="https://www.milidoc.vercel.app/favicon.ico"
          ></meta>
          <meta
            property="og:url"
            content="https://www.milidoc.vercel.app/"
          ></meta>

          <meta
            name="naver-site-verification"
            content="4f6863514cb56346924101a2bd08dd7079181e49"
          />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;
