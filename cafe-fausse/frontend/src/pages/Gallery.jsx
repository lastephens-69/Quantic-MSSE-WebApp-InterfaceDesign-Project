import React, { useMemo, useState } from "react";
import "./Gallery.css";

/**
 * Glob all images from any subfolder in /assets/cafe
 * (e.g., Dishes/, Catering/, Location/, Behind The Scenes/, etc.)
 */
const modules = import.meta.glob("/src/assets/cafe/*/*.{jpg,jpeg,png,webp}", {
  eager: true,
  as: "url",
});

// Helper: category = the immediate subfolder under /cafe/
function getCategory(url) {
  const parts = url.split("/");
  const idx = parts.indexOf("cafe");
  // e.g. /src/assets/cafe/Behind%20The%20Scenes/img.jpg -> "Behind%20The%20Scenes"
  return parts[idx + 1] || "Other";
}

// Helper: pretty display label from folder name
function displayLabel(raw) {
  // decode spaces (%20) and other encodings; then tidy up underscores/hyphens
  return decodeURIComponent(raw).replace(/[_-]+/g, " ").trim();
}

// 🔒 Desired display order for categories (edit to taste):
const ORDER = ["Location", "Dishes", "Catering", "Behind The Scenes"];

export default function Gallery() {
  const [active, setActive] = useState(null);
  const [filter, setFilter] = useState("All");

  // Group images by category (folder)
  const grouped = useMemo(() => {
    const byCat = {};
    Object.values(modules)
      .sort((a, b) => a.localeCompare(b))
      .forEach((url) => {
        const rawCat = getCategory(url);
        (byCat[rawCat] ??= []).push(url);
      });
    return byCat;
  }, []);

  // Build ordered category list for chips:
  // 1) start with ORDER (only those that exist), 2) then any others alphabetically
  const categories = useMemo(() => {
    const existing = Object.keys(grouped);
    const inOrder = ORDER.filter((name) => existing.includes(name));
    const remaining = existing
      .filter((name) => !ORDER.includes(name))
      .sort((a, b) => displayLabel(a).localeCompare(displayLabel(b)));
    return ["All", ...inOrder, ...remaining];
  }, [grouped]);

  // Sections to show (respecting the same order logic)
  const sections = useMemo(() => {
    if (filter !== "All") return [[filter, grouped[filter] || []]];
    const existing = Object.keys(grouped);
    const inOrder = ORDER.filter((name) => existing.includes(name)).map((name) => [name, grouped[name]]);
    const remaining = existing
      .filter((name) => !ORDER.includes(name))
      .sort((a, b) => displayLabel(a).localeCompare(displayLabel(b)))
      .map((name) => [name, grouped[name]]);
    return [...inOrder, ...remaining];
  }, [filter, grouped]);

  return (
    <div className="card">
      <h1>Gallery</h1>

      {/* Filter chips */}
      <div className="chips" role="tablist" aria-label="Filter gallery">
        {categories.map((c) => (
          <button
            key={c}
            role="tab"
            aria-selected={filter === c}
            className={`chip ${filter === c ? "active" : ""}`}
            onClick={() => setFilter(c)}
          >
            {c === "All" ? "All" : displayLabel(c)}
          </button>
        ))}
      </div>

      {/* Sections */}
      {sections.map(([rawCat, urls]) => (
        <section key={rawCat} className="gallery-section">
          {filter === "All" && <h3 className="gallery-heading">{displayLabel(rawCat)}</h3>}
          <div className="grid-gallery">
            {urls.map((src, i) => (
              <img
                key={src + i}
                className="gallery-img"
                src={src}
                alt={`${displayLabel(rawCat)} ${i + 1}`}
                loading="lazy"
                onClick={() => setActive(src)}
              />
            ))}
            {!urls?.length && <p className="empty">No images yet.</p>}
          </div>
        </section>
      ))}

      {/* Lightbox */}
      {active && (
        <div className="lightbox" onClick={() => setActive(null)} aria-modal="true" role="dialog">
          <img src={active} alt="Large view" />
        </div>
      )}
    </div>
  );
}
