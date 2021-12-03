# q2-cual-id

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

This is a QIIME 2 plugin. For details on QIIME 2, see https://qiime2.org.
