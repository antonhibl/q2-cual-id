# Q2-Cual-ID

---

### TO DO LIST

1. Implement semantic types for both the short and long ID (file?) formats

> This will allow me to convert between the two types using an action like cual transform
> also using one type in and out of an action like cual clean

2. define possible inputs to the actions (mostly done)

> Finish defining inputs and their descriptions for the common actions and methods in the plugin

3. Define some formats

> Define a way to store the ID information which should only need one universal encoding method
> Finish up defining directory formats
> What ways can we store the same info(this could swing me away from needing to define semantic types)

*Get Evan's opinion on the last point*

4. Define actions(traverse code from notebooks to scripts)

> After defining some actual actions in scripts, write tests
> clean up bugs and documentation after finished

5. Review with Evan and hopefully push into early testing online and start work on sphynx documentation.

---

# Documentation

---

__ID Generation__


> ID generation should be handled by the `cual_gen_pl()` function,
> this function is actually a pipeline that will establish and set-up
> an artifact with a file directory format which holds an ID file and
> it's relevant metadata.

> Another way to do this is to perform the actions of the pipeline
> yourself, or perhaps you simply want to generate these IDs as a
> simple array type data-structure in a scientific notebook; these
> are both possible by using the functions `generate_ids()` and
> `cual_transform()` by themselves or selectively.

__Fixing IDs__

> q2-cual-id packages up the ID File inside of a directory structure
> which also documents and stores metadata that is important when the
> plugin goes back to check and fix it's IDs if necessary. By
> attaching the metadata into the directory structure I can ensure
> users don't need to worry about the details of figuring out where
> the IDs to cross-reference against are, they can just pass in their
> artifact to the function and it handles the rest