// Public-safe Playwright smoke-test example for the Codiquiz preview/demo flow.
// This is a representative test file for portfolio review. It is not wired to run
// from this public repository because the full application source remains private.

import { expect, test } from "@playwright/test";

const PUBLIC_PREVIEW_URL = process.env.CODIQUIZ_PUBLIC_PREVIEW_URL ?? "https://preview.codiquiz.com";
const ADMIN_PREVIEW_URL = process.env.CODIQUIZ_ADMIN_PREVIEW_URL ?? "https://admin.preview.codiquiz.com";

test.describe("Codiquiz preview smoke checks", () => {
  test("public homepage loads", async ({ page }) => {
    await page.goto(PUBLIC_PREVIEW_URL);
    await expect(page).toHaveTitle(/Codiquiz/i);
    await expect(page.getByText(/Python/i).first()).toBeVisible();
  });

  test("admin login page loads without exposing owner-only content", async ({ page }) => {
    await page.goto(`${ADMIN_PREVIEW_URL}/login`);
    await expect(page.getByRole("button", { name: /log in|sign in/i })).toBeVisible();
    await expect(page.getByText(/OpenAI API key/i)).toHaveCount(0);
  });

  test("public technology page is reachable", async ({ page }) => {
    await page.goto(`${PUBLIC_PREVIEW_URL}/technology/python`);
    await expect(page.getByText(/Python/i).first()).toBeVisible();
    await expect(page.getByText(/Practice/i).first()).toBeVisible();
  });
});
