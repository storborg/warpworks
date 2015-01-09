require(['jquery', 'jquery.svg'], function ($) {

  var
    $svg,
    scale = 18,
    foreground = '#7f7f7f',
    background = '#ffffff',
    numbering = '#c80000',
    markers = '#000000',
    liftplan = true;

  function colorToCSS(color) {
    return 'rgba(' + color[0] + ', ' + color[1] + ', ' + color[2] + ', 1.0)';
  }

  function paintMarker(svg, parent, x, y) {
    svg.rect(parent, x + 2, y + 2, scale - 4, scale - 4, {fill: markers});
  }

  function paintWarp(svg, draft) {
    var
      ii, thread, x, y,
      g = svg.group({stroke: foreground});

    for(ii = 0; ii < draft.warp.length; ii++) {
      thread = draft.warp[ii];
      x = ii * scale;
      y = 0;
      svg.rect(g, x, y, scale, scale, {fill: colorToCSS(thread.color)});
    }
  }

  function paintWeft(svg, draft) {
    var
      ii, thread, x, y,
      g = svg.group({stroke: foreground}),
      yoffset = (6 + draft.num_shafts) * scale,
      xsquares = draft.warp.length + 5;

    if(liftplan || draft.liftplan) {
      xsquares += draft.num_shafts;
    } else {
      xsquares += draft.num_treadles;
    }

    x = xsquares * scale;

    for(ii = 0; ii < draft.weft.length; ii++) {
      thread = draft.weft[ii];
      y = (scale * ii) + yoffset;
      svg.rect(g, x, y, scale, scale, {fill: colorToCSS(thread.color)});
    }
  }

  function paintThreading(svg, draft) {
    var
      ii, jj, thread, x, y,
      g = svg.group({stroke: foreground, fill: background});

    for(ii = 0; ii < draft.warp.length; ii++) {
      thread = draft.warp[ii];
      x = (draft.warp.length - ii - 1) * scale;

      for(jj = 0; jj < draft.num_shafts; jj++) {
        y = (4 + (draft.num_shafts - jj)) * scale;

        svg.rect(g, x, y, scale, scale);

        if($.inArray(jj, thread.shafts) >= 0) {
          paintMarker(svg, g, x, y);
        }
      }

      // paint the number and marker if it's a multiple of 4
    }
  }

  function paintLiftplan(svg, draft) {
    var
      ii, jj, thread, x, y,
      g = svg.group({stroke: foreground, fill: background}),
      xoffset = (1 + draft.warp.length) * scale,
      yoffset = (6 + draft.num_shafts) * scale;

    for(ii = 0; ii < draft.weft.length; ii++) {
      thread = draft.weft[ii];
      y = (ii * scale) + yoffset;

      for(jj = 0; jj < draft.num_shafts; jj++) {
        x = (jj * scale) + xoffset;
        svg.rect(g, x, y, scale, scale);

        if($.inArray(jj, thread.shafts) >= 0) {
          paintMarker(svg, g, x, y);
        }
      }

      // paint the number and marker if it's a multiple of 4
    }
  }

  function paintTreadling(svg, draft) {
  }

  function paintTieup(svg, draft) {
  }

  function paintDrawdown(svg, draft) {
    // just paint a grid for now, we'll need another function to compute the drawdown
    var
      ii, jj, x, y,
      g = svg.group({stroke: foreground, fill: background}),
      yoffset = (6 + draft.num_shafts) * scale;

    for(ii = 0; ii < draft.warp.length; ii++) {
      x = ii * scale;
      for(jj = 0; jj < draft.weft.length; jj++) {
        y = (jj * scale) + yoffset;
        svg.rect(g, x, y, scale, scale);
      }
    }
  }

  function renderDraft(svg, draft) {
    paintWarp(svg, draft);
    paintWeft(svg, draft);
    paintThreading(svg, draft);
    if(liftplan || draft.liftplan) {
      paintLiftplan(svg, draft);
    } else {
      paintTreadling(svg, draft);
      paintTieup(svg, draft);
    }
    paintDrawdown(svg, draft);
  }

  $(function () {
    console.log('Loaded light/draft.');
    $('.section-draft').svg({
      onLoad: function(svg) {
        renderDraft(svg, window.draft);
      },
      settings: {
        width: 26 * scale,
        height: 26 * scale
      }
    });
  });
});
