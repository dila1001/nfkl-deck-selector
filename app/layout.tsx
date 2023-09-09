"use client";

import { useState } from "react";
import { MantineProvider } from "@mantine/core";
import Head from "next/head";
import NavbarMinimal from "./components/NavbarMinimal";
import {
  AppShell,
  Header,
  Text,
  MediaQuery,
  Burger,
  useMantineTheme,
} from "@mantine/core";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const theme = useMantineTheme();
  const [opened, setOpened] = useState(false);
  return (
    <html lang="en">
      <Head>
        <title>Deck selector</title>
        <meta property="og:title" content="Deck selector" key="title" />
        <meta property="og:description" content="Keyforge" key="description" />
      </Head>
      <MantineProvider withGlobalStyles withNormalizeCSS>
        <body>
          <AppShell
            styles={{
              main: {
                background:
                  theme.colorScheme === "dark"
                    ? theme.colors.dark[8]
                    : theme.colors.gray[0],
              },
            }}
            navbarOffsetBreakpoint="sm"
            navbar={
              <NavbarMinimal openState={opened} />
            }
            header={
              <Header height={{ base: 50, md: 70 }} p="md">
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    height: "100%",
                  }}
                >
                  <MediaQuery largerThan="sm" styles={{ display: "none" }}>
                    <Burger
                      opened={opened}
                      onClick={() => setOpened((o) => !o)}
                      size="sm"
                      color={theme.colors.gray[6]}
                      mr="xl"
                    />
                  </MediaQuery>

                  <Text>Deck selector - Keyforge</Text>
                </div>
              </Header>
            }
          >
            {children }
          </AppShell>
        </body>
      </MantineProvider>
    </html>
  );
}
