Converts QPC's mushaf v1 font files to SVGs ([sample](https://gist.github.com/mustafa0x/51f7197c371d4412a674f51f2ea16523?short_path=35eee4b#file-qpc-pg-003-svg)).

- The font files can be found in the [mushaf folder](https://github.com/mustafa0x/qpc-fonts)
- Requires `example2` from [font_to_svg](https://github.com/donbright/font_to_svg)

## Motivation
- SVG is a more accessible format, so improvements to the vectors can be easily made.
- Less buggy, less surprising behavior (the fonts sometimes break in browsers and under different corrects), less hacky.
- SVGs are (tentatively) more performant (e.g. Chrome freezes for a moment when rendering a ttf mushaf page)
- SVGs are a textual format. Text endures.

## Drawbacks
- The font files contained positioning information (mostly how wide each glyph should be -- especially important for pause marks), which hasn't yet been extracted. Even after extracting, embedding might be more difficult. Especially since SVGs aren't good at flowing text.
- TTFs are smaller (initial tests indicate around 15%, after optimizing the SVG file and brotli'ing both). With some effort the SVGs can be made smaller however.

## To Do
- Extract the positioning information so that the SVGs are usable. Approaches:
  - Convert the font files to ttx and derive the positioning from that
  - Use `Advance` in the comments to position the glyphs
  - Test other font->svg converters
  - Convert to PDF then to HTML to derive coordinates
- Break at ayah lines
- Replace ayah mark vectors with Unicode ayah marks
- Remove the small لا pause mark
- Compress with SVGO
- Improve the vectors (remastering)
