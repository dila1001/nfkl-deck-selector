"use client";

import { useState } from "react";
import {
  Navbar,
  Tooltip,
  UnstyledButton,
  createStyles,
  Stack,
  rem,
} from "@mantine/core";
import {
  IconHome2,
  IconSettings,
  IconLogout,
  IconCards,
  IconShirtSport,
  IconUserHexagon,
  IconDeviceAnalytics,
  IconDeviceGamepad2,
} from "@tabler/icons-react";
import { usePathname, useRouter } from "next/navigation";

const useStyles = createStyles((theme) => ({
  link: {
    width: rem(50),
    height: rem(50),
    borderRadius: theme.radius.md,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[0]
        : theme.colors.gray[7],

    "&:hover": {
      backgroundColor:
        theme.colorScheme === "dark"
          ? theme.colors.dark[5]
          : theme.colors.gray[0],
    },
  },

  active: {
    "&, &:hover": {
      backgroundColor: theme.fn.variant({
        variant: "light",
        color: theme.primaryColor,
      }).background,
      color: theme.fn.variant({ variant: "light", color: theme.primaryColor })
        .color,
    },
  },
}));

interface NavbarLinkProps {
  icon: React.FC<any>;
  label: string;
  active?: boolean;
  onClick?(): void;
}

function NavbarLink({ icon: Icon, label, active, onClick }: NavbarLinkProps) {
  const { classes, cx } = useStyles();
  return (
    <Tooltip label={label} position="right" transitionProps={{ duration: 0 }}>
      <UnstyledButton
        onClick={onClick}
        className={cx(classes.link, { [classes.active]: active })}
      >
        <Icon size="1.2rem" stroke={1.5} />
      </UnstyledButton>
    </Tooltip>
  );
}

const linkData = [
  { icon: IconHome2, label: "Home", route: "/" },
  { icon: IconDeviceGamepad2, label: "Games", route: "/games" },
  { icon: IconCards, label: "Decks", route: "/decks" },
  { icon: IconShirtSport, label: "Divisions", route: "/divisions" },
  { icon: IconDeviceAnalytics, label: "Statistics", route: "/statistics" },
  { icon: IconUserHexagon, label: "Admin", route: "/admin" },
];

export default function NavbarMinimal({ openState }: { openState: boolean}) {
  const pathName = usePathname();
  let startIndex = 0;
  linkData.forEach((link, index) => {
    if (link.route === pathName){
      startIndex = index;
      return;
    }
  });

  const [active, setActive] = useState(startIndex);
  const router = useRouter();

  const handleClick = (route: string, index: number) => {
    router.push(route);
    setActive(index);
  };

  const links = linkData.map((link, index) => (
    <NavbarLink
      {...link}
      key={link.label}
      active={index === active}
      onClick={() => handleClick(link.route, index)}
    />
  ));

  return (
    <Navbar
      width={{ sm: 82, md: 82 }}
      p="md"
      hiddenBreakpoint="sm"
      hidden={!openState}
    >
      <Navbar.Section grow>
        <Stack justify="center" spacing={0}>
          {links}
        </Stack>
      </Navbar.Section>
      <Navbar.Section>
        <Stack justify="center" spacing={0}>
          <NavbarLink icon={IconSettings} active={6 === active} label="Settings" onClick={() => handleClick("/profile", 6)} />
          <NavbarLink icon={IconLogout} label="Logout" />
        </Stack>
      </Navbar.Section>
    </Navbar>
  );
}
