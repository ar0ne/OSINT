"use client"

import { useRouter } from 'next/navigation';
import { createScan } from "@/app/lib/actions";
import Button from "@/app/ui/button";
import { useFormStatus, useFormState } from 'react-dom';
import styles from "@/app/ui/card/card.module.css";


export default function Form({onClose}) {

  const initialState = {message: null, errors: {}};
  const [state, formAction] = useFormState(createScan, initialState);
  const router = useRouter();
  const formActionAndUpdate = async (data) => {
    formAction(data);
    router.refresh();
    onClose();
  };

  // TODO: take it from 
  const TOOLS = ["theHarvester"];

  if (!state) return;
  
  return (
    <form 
      action={formActionAndUpdate}
      className={styles.form}
      >
      <div>
        <div>
          <label htmlFor="tool">
            Choose a tool for scanning
          </label>
          <div>
            <select 
              id="tool"
              name="tool"
              defaultValue=""
              aria-describedby="tool-error"
            >
            <option value="" disabled>
              Select a tool
            </option>
            {TOOLS.map((t) => (
              <option key={t} value={t}>
                {t}
              </option>
            ))}
            </select>
          </div>

          <div id="tool-error" aria-live="polite" aria-atomic="true">
            {state.errors?.tool &&
              state.errors.tool.map((error) => (
                <p className="" key={error}>
                  {error}
                </p>
              ))}
          </div>
        </div>

        <div>
          <div>
            <label htmlFor="tool">
              Choose a domain to scan
            </label>
            <div>
              <input
                id="domain"
                name="domain"
                type="string"
                placeholder="example.com"
                aria-describedby="domain-error"
              />
            </div>
          </div>
          
          <div id="domain-error" aria-live="polite" aria-atomic="true">
            {state.errors?.domain &&
              state.errors.domain.map((error) => (
                <p className="" key={error}>
                  {error}
                </p>
              ))}
          </div>

          <div aria-live="polite" aria-atomic="true">
            {state.message ? (
              <p className="mt-2 text-sm text-red-500">{state.message}</p>
            ) : null}
          </div>

        </div>
        <Button type="submit">Start scan</Button>
      </div>
    </form>
  );
}
