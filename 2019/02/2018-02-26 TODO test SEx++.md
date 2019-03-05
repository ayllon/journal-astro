* Check if weight is convolved in SEx++
    - There are differences on the borders, which is where there is a sharp
      change. That's precisely where lack of convolution is evident
* Filter magnitudes 99 (nan)
    - DONE for coadd
* Force $\Delta$ plot to be $\pm 1$, otherwise it is hard to see relevant points (DONE)
    - Show arrows to let know there are values outside (DONE)
* KS comparision is good for first order
* *Completeness* and *pureness*
    - How many real sources have been detected (completeness)
    - How many of the detected are real (pureness)
    - Bin per magnitude
    - Separate for galaxies and stars
    - Test can be "80% at least"
    - SEx2 aparently is so-so at this, so SEx++ is only expected to be as so-so
* Plot distance histograms splitting for $\alpha$ and $\delta$ (DONE)
* Scatter $\Delta x$ and $\Delta y$ vs magnitude
* Scatter $\Delta \alpha$ and $\Delta \delta$ vs magnitude (DONE)
* Measure background per source
    - Background model interpolation at the centroid of the source
    - Plot vs x and y
    - Comparing SEx2 and SEx++!

**NOTE**: There seems to be a leak when using moffat splitting, or, at least,
    a hell of a lot of memory is used. Eventually SEx++ crashes with a SIGSEGV
    inside Levmar called by FlexibleModelFitting. No crash without MOFFAT grouping,
    no crash if I reduce the number of iterations (which seems ignored by Flexible).
    Smells like race condition or leak, or both.
    
Neither, MOFFAT is causing the grouping of *a lot* of sources (O(100)) with the default
configuration on sim09. That causes an explosion on the number of parameters and residuals
when doing the model fitting. Since levmar tries to allocate as much memory as
O(number of parameters * number of residuals), with the number of residuals being as many
as involved pixels, that blows up, requiring the allocation of a lot of memory.

On top of that, levmar uses a signed 32 bits int for the multiplication, so sometimes
it wraps to a negative number, and malloc fails to allocate.
