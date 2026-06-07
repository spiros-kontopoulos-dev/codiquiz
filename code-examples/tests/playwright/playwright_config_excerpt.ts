// Playwright configuration excerpt
// Source: frontend/playwright.config.ts (excerpt lines 1-41)
// Public portfolio excerpt; not standalone application code.

import { defineConfig, devices } from "@playwright/test";

const baseURL = process.env.PLAYWRIGHT_BASE_URL ?? "http://localhost:5173";

// Playwright is the browser-level QA safety net. It is intentionally focused on
// full user workflows, while backend algorithms and API behavior should also get
// pytest coverage later. Keep Docker Compose running before these tests so the
// frontend can call quiz-api normally.
export default defineConfig({
  testDir: "./e2e",
  timeout: 30_000,
  expect: {
    timeout: 10_000,
  },
  fullyParallel: false,
  retries: process.env.CI ? 1 : 0,
  reporter: [
    ["list"],
    ["html", { outputFolder: "playwright-report", open: "never" }],
  ],
  use: {
    baseURL,
    trace: "on-first-retry",
    screenshot: "only-on-failure",
    video: "retain-on-failure",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],
  webServer: process.env.PLAYWRIGHT_SKIP_WEB_SERVER
    ? undefined
    : {
        command: "npm run dev -- --host 0.0.0.0",
        url: baseURL,
        reuseExistingServer: true,
        timeout: 120_000,
      },
});
