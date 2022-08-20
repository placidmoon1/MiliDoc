import { Spinner } from "@chakra-ui/react";

const Loader = () => {
  return (
    <div
      style={{
        minHeight: "100vh",
        width: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Spinner
          thickness="4px"
          speed="0.65s"
          emptyColor="gray.200"
          color="#026ddd"
          size="xl"
        />
        <h1 style={{
            marginTop: "1rem",
            fontSize: "1.1rem",
            fontWeight: "600"
        }}>로딩중...</h1>
      </div>
    </div>
  );
};

export default Loader;